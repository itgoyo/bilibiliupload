from ..engine.upload import UploadBase, logger
from ..engine import Plugin


@Plugin.upload(platform="Noop")
class NoopUploader(UploadBase):
    def upload(self, file_list):
        logger.info("NoopUploader")
        return file_list
