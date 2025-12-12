package docker.security

deny[msg] {
  input.kind == "Dockerfile"
  not input.user
  msg := "Dockerfile must specify a USER instruction"
}

deny[msg] {
  input.kind == "Dockerfile"
  input.user == "root"
  msg := "Dockerfile must not run as root user"
}
