broker_url = "pyamqp://guest@localhost//"
result_backend = "redis://localhost"

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "Asia/Seoul"
enable_utc = True
task_routes = {
    "tasks.add": "low-priority",
}
task_annotations = {"tasks.add": {"rate_limit": "10/m"}}
