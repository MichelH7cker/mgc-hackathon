resource "mgc_virtual_machine_instances" "nexgen-front" {
  name     = "nexgen-front"
  machine_type = {
    name = "cloud-bs1.xsmall"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = true # If true, will create a public IP
    delete_public_ip    = false
  }

  ssh_key_name = "michel"
}

resource "mgc_virtual_machine_instances" "nexgen-back" {
  name     = "nexgen-back"
  machine_type = {
    name = "cloud-bs1.xsmall"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = true # If true, will create a public IP
    delete_public_ip    = false
  }

  ssh_key_name = "michel"
}
