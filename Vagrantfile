Vagrant.configure("2") do |config|

  config.vm.define "ansible" do |ansible|
    ansible.vm.box = "bento/centos-7.3"
    ansible.vm.hostname = 'vagrant'
    ansible.vm.provision :shell, path: "vagrant_bootstrap.sh"
  end

end
