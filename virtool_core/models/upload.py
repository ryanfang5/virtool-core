from datetime import datetime
from typing import Optional, List

from virtool_core.models.basemodel import BaseModel
from virtool_core.models.user import UserMinimal


class UploadMinimal(BaseModel):
    """
    Model for user uploads.
    """

    id: int
    created_at: datetime
    name: str
    name_on_disk: str
    ready: bool
    removed: bool
    removed_at: Optional[datetime]
    reserved: bool
    size: int
    type: str
    uploaded_at: datetime
    user: UserMinimal


Upload = UploadMinimal


class UploadSearchResult(BaseModel):
    documents: List[UploadMinimal]
