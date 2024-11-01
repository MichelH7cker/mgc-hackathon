TF_EXAMPLE = """    
    resource "mgc_virtual_machine_instances" "<name>" {
    name     = "<name>"
    machine_type = {
        name = "BV2-2-40"
    }
    image = {
        name = ""
    }
    network = {
        associate_public_ip = true # If true, will create a public IP
        delete_public_ip    = false
    }

    ssh_key_name = "<ssh_key>"
    }

    resource "mgc_virtual_machine_instances" "<name>" {
    name     = "<name>"
    machine_type = {
        name = "BV2-2-40"
    }
    image = {
        name = ""
    }
    network = {
        associate_public_ip = true # If true, will create a public IP
        delete_public_ip    = false
    }

    ssh_key_name = "<ssh_key>"
    }

    provider "mgc" {
    region = var.mgc_region
    api_key = var.mgc_api_key
    object_storage = {
        key_pair = {
        key_id = var.mgc_obj_key_id
        key_secret = var.mgc_obj_key_secret
        }
    }
    }

    variable "mgc_api_key" {
    type = string
    description = "Chave da Magalu Cloud"
    sensitive = true
    nullable = false
    }

    variable "mgc_obj_key_id" {
    type = string
    description = "ID da Chave do Object Storage"
    sensitive = true
    nullable = false
    }

    variable "mgc_obj_key_secret" {
    type = string
    description = "Secret da Chave do Object Storage"
    sensitive = true
    nullable = false
    }

    variable "mgc_region" {
    type = string
    description = "Região da Magalu Cloud"
    sensitive = true
    nullable = false
    }

    terraform {
    required_providers {
        mgc = {
        source = "magalucloud/mgc"
        version = "0.23.0"
        }
        local = {
        source  = "hashicorp/local"
        version = "2.5.1"
        }
    }
    }
"""