# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


Streaming_job_pipeline = Job.from_dict(
    {
        "name": "Streaming_job_pipeline",
        "continuous": {
            "pause_status": "PAUSED",
            "task_retry_mode": "ON_FAILURE",
        },
        "tasks": [
            {
                "task_key": "bronze_kline",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/nguyenvietduc1410@outlook.com/Real-time-Crypto-Market-Analytics-Lakehouse/notebooks/bronze/bronze_kline",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "bronze_trade",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/nguyenvietduc1410@outlook.com/Real-time-Crypto-Market-Analytics-Lakehouse/notebooks/bronze/bronze_trade",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "pull_data_from_kafka",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/nguyenvietduc1410@outlook.com/Real-time-Crypto-Market-Analytics-Lakehouse/notebooks/ingest/Kafka_to_Raw_Landing",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "silver_kline",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/nguyenvietduc1410@outlook.com/Real-time-Crypto-Market-Analytics-Lakehouse/notebooks/silver/Silver_kline",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "silver_trade",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/nguyenvietduc1410@outlook.com/Real-time-Crypto-Market-Analytics-Lakehouse/notebooks/silver/Silver_trades",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "gold_layer",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/nguyenvietduc1410@outlook.com/Real-time-Crypto-Market-Analytics-Lakehouse/notebooks/gold/Gold",
                    "source": "WORKSPACE",
                },
            },
        ],
        "queue": {
            "enabled": True,
        },
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.jobs.reset(new_settings=Streaming_job_pipeline, job_id=369199812689559)
# or create a new job using: w.jobs.create(**Streaming_job_pipeline.as_shallow_dict())
