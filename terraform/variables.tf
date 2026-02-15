variable "docker_username" {
  description = "도커 허브 사용자 이름"
  type        = string
  default     = "osw1014"
}

variable "project_name" {
  type    = string
  default = "my-k8s-project"
}

variable "external_port" {
  description = "외부에서 접속할 포트 번호"
  type        = number
  default     = 8080
}