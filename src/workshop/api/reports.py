from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import StreamingResponse

from ..models.auth import User
from ..services.auth import get_current_user
from ..services.reports import ReportsService

router = APIRouter(prefix='/reports', tags=["Reports", ])


@router.post('/import')
def import_csv(
        file: UploadFile = File(...),
        user: User = Depends(get_current_user),
        reports_service: ReportsService = Depends()
):
    return reports_service.import_csv(user_id=user.id, file=file.file)


@router.get('/export')
def export_csv(
        user: User = Depends(get_current_user),
        reports_service: ReportsService = Depends()
):
    report = reports_service.export_csv(user.id)
    return StreamingResponse(
        report,
        media_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename=report.csv'}
    )
