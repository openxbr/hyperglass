"""hyperglass global state."""

# Standard Library
import typing as t

# Third Party
from redis import Redis, ConnectionPool

# Project
from hyperglass.configuration import params, devices, ui_params

# Local
from .redis import RedisManager

if t.TYPE_CHECKING:
    # Project
    from hyperglass.models.system import HyperglassSystem


class StateManager:
    """Global State Manager.

    Maintains configuration objects in Redis cache and accesses them as needed.
    """

    settings: "HyperglassSystem"
    redis: RedisManager
    _namespace: str = "hyperglass.state"

    def __init__(self, *, settings: "HyperglassSystem") -> None:
        """Set up Redis connection and add configuration objects."""

        self.settings = settings
        connection_pool = ConnectionPool.from_url(**self.settings.redis_connection_pool)
        redis = Redis(connection_pool=connection_pool)
        self.redis = RedisManager(instance=redis, namespace=self._namespace)

        # Add configuration objects.
        self.redis.set("params", params)
        self.redis.set("devices", devices)
        self.redis.set("ui_params", ui_params)

    @classmethod
    def properties(cls: "StateManager") -> t.Tuple[str, ...]:
        """Get all read-only properties of the state manager."""
        return tuple(
            attr
            for attr in dir(cls)
            if not attr.startswith("_") and "fget" in dir(getattr(cls, attr))
        )