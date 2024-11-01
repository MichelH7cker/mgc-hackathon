resource "mgc_virtual_machine_instances" "nexgen-front-neww" {
  name = "nexgen-front-neww"
  machine_type = {
    name = "BV2-2-40"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = true # If true, will create a public IP
    delete_public_ip    = false
  }

  ssh_key_name = "fabricio"
}

resource "mgc_virtual_machine_instances" "nexgen-back-neww" {
  name = "nexgen-back-neww"
  machine_type = {
    name = "BV2-2-40"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = true # If true, will create a public IP
    delete_public_ip    = false
  }

  ssh_key_name = "fabricio"

    

  provisioner "file" {
    source      = "../site/backend"
    destination = "~/"
  }
  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update -y",
      "sudo apt-get install -y python3-pip",
      "pip3 install -r ~/backend/requirements.txt -y",
      "python3 app.py" 
    ]
  }
  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("~/.ssh/id_rsa")
    host        = self.network.public_address
  }
}
