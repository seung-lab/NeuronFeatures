from email.mime import base
from neuronfeatures.packages.base import BasePackage


class Package(BasePackage):
    feature_columns = {
        "skeleton_h5": {"in_datastore": False},
        "skeleton_swc": {"in_datastore": False},
        "total_pathlength_nm": {"in_datastore": True},
    }
    package_name = "skeletons"

    def __init__(self, invalidation_ball_distance_nm, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._invalidation_ball_distance_nm = invalidation_ball_distance_nm

    @property
    def invalidation_ball_distance_nm(self):
        return self._invalidation_ball_distance_nm
