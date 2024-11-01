resource "mgc_virtual_machine_instances" "nexgen-front-new-test" {
  name = "nexgen-front-new-test"
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

  ssh_key_name = "michel"

  provisioner "file" {
    source      = "../site/frontend/"
    destination = "~/"
  }
  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update -y",
      "sudo apt-get install -y python3-pip",
      "curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -",
      "sudo apt install -y nodejs",
      "cd ../site/frontend",
      "npm install",
      "npm run dev",
    ]
  }
  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("~/.ssh/id_rsa")
    host        = self.network.public_address
  }

}

//resource "mgc_virtual_machine_instances" "nexgen-back-neww" {
//  name = "nexgen-back-neww"
//  machine_type = {
//    name = "BV2-2-40"
//  }
//  image = {
//    name = "cloud-ubuntu-22.04 LTS"
//  }
//  network = {
//    associate_public_ip = true # If true, will create a public IP
//    delete_public_ip    = false
//  }
//
//  ssh_key_name = "michel"
//
//  provisioner "file" {
//    source      = "../site/backend"
//    destination = "~/"
//  }
//  provisioner "remote-exec" {
//    inline = [
//      "sudo apt-get update -y",
//      "sudo apt-get install -y python3-pip",
//      "pip3 install -r ~/backend/requirements.txt -y",
//      "python3 app.py" 
//    ]
//  }
//  connection {
//    type        = "ssh"
//    user        = "ubuntu"
//    private_key = file("~/.ssh/id_rsa")
//    host        = self.network.public_address
//  }
//}
