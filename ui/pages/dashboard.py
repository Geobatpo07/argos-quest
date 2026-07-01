# ./ui/pages/dashboard.py

from application.services.statistics_service import StatisticsService
from application.services.synchronization_service import SynchronizationService

from ui.components.alerts import success
from ui.components.buttons import primary_button
from ui.components.layout import page, section
from ui.components.metrics import metrics


def show_dashboard():

    page(
        title="Dashboard",
        icon="🏠",
        description="Overview of your PhD opportunity tracker.",
    )

    section("Synchronization")

    if primary_button(
        "Synchronize opportunities",
        icon="🔄",
    ):

        imported = (
            SynchronizationService()
            .synchronize()
        )

        success(
            f"{imported} opportunities synchronized."
        )

    section("Overview")

    dashboard = (
        StatisticsService()
        .dashboard()
    )

    metrics(dashboard)