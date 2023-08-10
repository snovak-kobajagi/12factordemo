init:
    terraform init

validate:
    terraform fmt -recursive
    terraform validate

plan:
    terraform validate
    terraform plan -var-file="variables.tfvars"

apply:
    terraform apply -var-file="variables.tfvars"

destroy:
    terraform destroy -var-file="variables.tfvars"

all: validate plan apply