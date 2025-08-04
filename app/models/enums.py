import enum

class StatusEnum(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class RoleEnum(enum.Enum):
    USER = "user"
    ADMIN = "admin"
    MODERATOR = "moderator"


class PlatformEnum(enum.Enum):
    YOUTUBE = "youtube"
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    TWITTER = "twitter"


class AssetTypeEnum(enum.Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"


class AgreementTypeEnum(enum.Enum):
    TERMS_OF_SERVICE = "terms_of_service"
    PRIVACY_POLICY = "privacy_policy"
    USER_AGREEMENT = "user_agreement"


class UploadStatusEnum(enum.Enum):
    UPLOADING = "uploading"
    COMPLETED = "completed"
    FAILED = "failed"
    PROCESSING = "processing"