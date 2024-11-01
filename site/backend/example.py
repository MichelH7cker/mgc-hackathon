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

TF_EXAMPLE_VM = """
terraform {
  required_providers {
    mgc = {
      source = "magalucloud/mgc"
    }
  }
}

# Create a volume 
resource "mgc_block_storage_volumes" "example_volume" {
  provider = mgc.nordeste
  name = "example-volume"
  size = 10
  type = {
    name = "cloud_nvme"
  }
}

# Create a VM at Nordeste br-ne1
resource "mgc_virtual_machine_instances" "basic_instance_nordeste" {
  provider = mgc.nordeste # We specify the provider region here to indicate that this VM should be created in the Nordeste region.
  name = "basic-instance-nordeste"
  machine_type = {
    name = "cloud-bs1.xsmall"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = false # If true, will create a public IP
  }
  delete_public_ip = false
  ssh_key_name   = var.ssh_key_name
}

# Attaching the VM with Block Storage
resource "mgc_block_storage_volume-attachment" "attached_block_storage" {
  block_storage_id = mgc_block-storage_volumes.example_volume.id
  virtual_machine_id = mgc_virtual-machine_instances.basic_instance_nordeste.id
}

output "basic_intance_id" {
  value = mgc_virtual-machine_instances.basic_instance_nordeste.id
}

output "bs_id" {
  value = mgc_block-storage_volumes.example_volume.id
}

provider "mgc" {
  alias = "sudeste"
  region = "br-se1"
  api_key = "your-api-key"
}

provider "mgc" {
  alias = "nordeste"
  region = "br-ne1"
  api_key = "your-api-key"
}

variable "ssh_key_name" {
  description = "SSH Key Name"
  type        = string
  default     = "SSH-KEY"
}
"""

TF_EXAMPLE_KUBERNETS = """
# Criando um cluster com um nodepool
resource "mgc_kubernetes_cluster" "cluster" {
  name                 = var.cluster_name
  version              = var.kubernetes_version
  enabled_server_group = false
  description          = var.cluster_description
}


# Criando um nodepool
resource "mgc_kubernetes_nodepool" "gp1_small" {
  depends_on = [mgc_kubernetes_cluster.cluster_with_nodepool]
  name       = "apis-2cpu-4gb-20gb"
  cluster_id = mgc_kubernetes_cluster.cluster_with_nodepool.id
  flavor     = var.nodepool_flavor
  replicas   = var.nodepool_replicas
  auto_scale = {
    min_replicas = 1
    max_replicas = 3
  }
}


# Pegar o kubeconfig do cluster usando o output do cluster_id
data "mgc_kubernetes_cluster_kubeconfig" "cluster" {
  depends_on = [time_sleep.wait_for_cluster]
  cluster_id = mgc_kubernetes_cluster.cluster_with_nodepool.id
}

# Salvar o kubeconfig em um arquivo local
resource "local_file" "kubeconfig" {
  provider = local
  content  = data.mgc_kubernetes_cluster_kubeconfig.cluster.kubeconfig
  filename = "${path.module}/kubeconfig.yaml"
}

output "cluster_name" {
  value = mgc_kubernetes_cluster.cluster_with_nodepool.name
}
output "cluster_id" {
  value = mgc_kubernetes_cluster.cluster_with_nodepool.id
}

variable "cluster_name" {
  description = "Cluster name"
  type        = string
  default     = "mgc-cluster"
}

variable "kubernetes_version" {
  description = "Kubernetes version"
  type        = string
  default     = "v1.28.5"
}

variable "cluster_description" {
  description = "Cluster description"
  type        = string
  default     = "A Kubernetes cluster managed by Magalu Cloud."
}

variable "nodepool_name" {
  description = "Nodepool name"
  type        = string
  default     = "mgc-nodepool"
}

variable "nodepool_replicas" {
  description = "Number of nodepool replicas"
  type        = number
  default     = 1
}

variable "nodepool_flavor" {
  description = "Nodepool flavor"
  type        = string
  default     = "cloud-k8s.gp1.small"
}

variable "timer_duration" {
  description = "Timer duration"
  type        = string
  default     = "15m"
}

terraform {
  required_providers {
    mgc = {
      source = "magalucloud/mgc"
    }
    local = {
      source  = "hashicorp/local"
      version = "2.5.1"
    }
  }
}
"""
