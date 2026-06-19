from datetime import datetime, timedelta

class Investment:
    def __init__(self, value: float, duration_days: int, rate: float = 0.05):
        self._value = value
        self._rate = rate
        self._duration_days = duration_days
        self._start_date = datetime.now() - timedelta(days=duration_days)

    @property
    def end_date(self):
        return self._start_date + timedelta(days=self._duration_days)

    @property
    def is_mature(self):
        return datetime.now() >= self.end_date

    @property
    def current_value(self):
        months = self._duration_days / 30
        return self._value * (1 + self._rate) ** months

    @property
    def rate(self):
        return self._rate

    def _increase_interest(self, value: float | int):
        if not isinstance(value, (float, int)):
            raise ValueError('Invalid value.')
        if value <= 0:
            raise ValueError('Rate must be positive.')
        self._rate = value
        