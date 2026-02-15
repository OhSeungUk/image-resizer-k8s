output "access_url" {
  description = "접속 가능한 주소"
  value       = "http://localhost:${var.external_port}"
}

output "container_name" {
  value = docker_container.frontend_server.name
}