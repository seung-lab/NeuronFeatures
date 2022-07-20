import caveclient


class BasePackage:
    feature_columns = {
        "light_feature_name": {"in_datastore": True},
        "heavy_feature_name": {"in_datastore": False},
    }
    package_name = "base"

    def __init__(
        self, base_path, datastack_name, server_address=None, auth_token=None
    ) -> None:
        self._base_path = base_path
        self._datastack_name = datastack_name
        self._cave_client = caveclient.CAVEclient(
            self._datastack_name, server_address=server_address, auth_token=auth_token
        )

    @property
    def cave_client(self):
        return self._cave_client

    @property
    def base_path(self):
        return self._base_path

    @property
    def datastack_name(self):
        return self._datastack_name

    @property
    def datastore_flex_config(self):
        config = {}
        for column_name, column in self.feature_columns.items():
            if not column["in_datastore"]:
                config[column_name] = {
                    "bucket_path": f"{self.base_path}/{self.package_name}/{column_name}",
                    "path_elements": ["root_id"],
                }
        return config

    def compute(self, root_ids, save=True):
        raise NotImplementedError(
            f"Package {self.package_name} has no compute function."
        )

    def save(self, data):
        pass

    def load(self, root_ids):
        pass
