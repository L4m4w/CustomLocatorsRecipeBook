import time
from typing import Callable
from typing import Generic
from typing import Literal
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.types import WaitExcTypes
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

POLL_FREQUENCY: float = 0.5  # How long to sleep in between calls to the method
IGNORED_EXCEPTIONS: Tuple[Type[Exception]] = (NoSuchElementException,)  # default to be ignored.

D = TypeVar("D", bound=Union[WebDriver, WebElement])
T = TypeVar("T")


class WebDriverWait(Generic[D]):
    def __init__(
        self,
        driver: D,
        timeout: float,
        poll_frequency: float = POLL_FREQUENCY,
        ignored_exceptions: Optional[WaitExcTypes] = None,
    ):

        self._driver = driver
        self._timeout = float(timeout)
        self._poll = poll_frequency
        # avoid the divide by zero
        if self._poll == 0:
            self._poll = POLL_FREQUENCY
        exceptions = list(IGNORED_EXCEPTIONS)
        if ignored_exceptions:
            try:
                exceptions.extend(iter(ignored_exceptions))
            except TypeError:  # ignored_exceptions is not iterable
                exceptions.append(ignored_exceptions)
        self._ignored_exceptions = tuple(exceptions)

    def __repr__(self):
        return f'<{type(self).__module__}.{type(self).__name__} (session="{self._driver.session_id}")>'

    def until(self, method: Callable[[D], Union[Literal[False], T]], message: str = "") -> T:
        screen = None
        stacktrace = None
        reason_msg = None

        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
                reason_msg = getattr(exc, "msg", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
        raise TimeoutException(message + ' ' + reason_msg, screen, stacktrace)
