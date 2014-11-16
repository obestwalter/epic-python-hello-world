Vagrant.configure("2") do |config|
    config.vm.define "phusion" do |p|
        p.vm.provider "docker" do |d|
            d.build_dir = "."
            d.has_ssh = true
        end
        p.ssh.username = "root"
        # https://raw.githubusercontent.com/phusion/baseimage-docker/master/image/insecure_key
        p.ssh.private_key_path = "insecure_key"
        p.vm.provision "shell", inline: "echo Epic Hello World"
        # p.vm.synced_folder "/bla", /blubb
    end
end
