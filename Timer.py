import threading
from typing import Callable, Optional


class ThreadTimer:
    """
    Таймер, работающий в отдельном потоке без использования QTimer.

    Поддерживает:
    - Однократное срабатывание (single_shot=True)
    - Периодический режим (single_shot=False)
    - Потокобезопасную остановку
    - Автоматическую очистку ресурсов
    """

    def __init__(self):
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._lock = threading.Lock()
        self._running = False
        self._single_shot = True
        self._duration = 0.0
        self._callback: Optional[Callable] = None

    def start(
        self, duration: float, callback: Callable, single_shot: bool = True
    ) -> None:
        """
        Запуск таймера.

        :param duration: Время в секундах (может быть дробным, например 0.5)
        :param callback: Функция, которая будет вызвана по истечении времени
        :param single_shot: True для однократного срабатывания, False для периодического
        """
        if duration < 0:
            raise ValueError("Время должно быть неотрицательным")

        self.stop()

        with self._lock:
            self._stop_event.clear()
            self._running = True
            self._single_shot = single_shot
            self._duration = duration
            self._callback = callback
            self._thread = threading.Thread(
                target=self._worker,
                daemon=True,
            )
            self._thread.start()

    def stop(self) -> None:
        """Немедленная остановка таймера без вызова коллбэка."""
        with self._lock:
            if not self._running:
                return
            self._running = False
            self._stop_event.set()

        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)

    def _worker(self) -> None:
        """Внутренний метод-воркер для периодического или однократного выполнения."""
        while True:
            # Ожидание с возможностью прерывания
            interrupted = self._stop_event.wait(timeout=self._duration)

            with self._lock:
                should_trigger = not interrupted and self._running
                if interrupted or not self._running:
                    self._running = False
                    break

                # Для однократного режима останавливаем таймер после срабатывания
                if self._single_shot:
                    self._running = False

            if should_trigger and self._callback:
                try:
                    self._callback()
                except Exception as e:
                    print(f"Ошибка в коллбэке таймера: {e}")

            # В периодическом режиме продолжаем цикл
            if self._single_shot:
                break

    @property
    def is_running(self) -> bool:
        """Проверка, запущен ли таймер в данный момент."""
        with self._lock:
            return self._running

    def set_interval(self, duration: float) -> None:
        """
        Изменение интервала для периодического таймера.
        Требует перезапуска таймера для применения изменений.
        """
        with self._lock:
            self._duration = duration
