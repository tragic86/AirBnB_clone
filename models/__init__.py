from models.engine.file_storage import FileStorage

__all__ = ["amenity","base_model","city",
		   "place","review","state", "user", "User"]

storage = FileStorage()
storage.reload()