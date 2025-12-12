package main

approved_images := [
  "python:3.11-slim",
  "nginx:1.27-alpine"
]

deny[msg] {
  input.kind == "Dockerfile"
  not approved_base_image
  msg := sprintf("Base image '%s' is not in approved list", [input.base_image])
}

approved_base_image {
  approved_images[_] == input.base_image
}
