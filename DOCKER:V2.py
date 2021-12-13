import os


print("""
		#########################################
		#                                       #
		#                                       #
		#               DOCKER                  #
		#                                       #
		#########################################

		_________________________________________
		_________________________________________
""")

while True:
	print("""
	1.To install docker                  13.To delete all the images
	2.To start docker services           14.To create an image
	3.Login to dockerhub                 15.To save an image
	4.docker information                 16.To load an image
	5.To download docker images          17.To change image name
	6.To launch docker container         18.Upload image to docker registry
	7.To copy a file inside container    19.Details of image/container
	8.To see running containers          20.To run a cmd and exit 
	9.To see all containers              21.To list all networks
	10.To delete a container             22.To inspect any network
	11.To delete all the containers      23.To check history of images
	12.To delete any image               24. For main menu
	""")
	ch =int(input("Enter your choice: "))
	if ch == 1:
		os.system("yum install -y yum-utils")
		os.system("yum-config-manager \
		--add-repo \
		https://download.docker.com/linux/centos/docker-ce.repo")
		os.system("yum install docker-ce -y -y")

	elif ch == 2:
		os.system("systemctl start docker")

	elif ch == 3:
		os.system("docker login")

	elif ch == 4:
		os.system("docker info")	



	elif ch == 5:
		img = input("Enter image name: ")
		os.system("docker pull {}".format(img))

	elif ch == 6:
		img =input("Enter image name:")
		env =input("Want any environmental variable(y/n): ")
		if env == "n":
			gui =input("Want to run GUI programs(y/n): ")
			if gui == "n":
				pat = input("Want to have patting enabled?(y/n): ")
				if pat == "n":
					mount = input("want to link storage to docker host(y/n): ")
					if mount == "n":
						name = input("Enter your container name: ")
						os.system("docker run -it --name {} {}".format(name,img))
					elif mount == "y":
						h_path = input("docker host path: ")
						c_path = input("container path: ")
						name = input("Enter your container name: ")
						os.system("docker run -it --name {} -v {}:{}  {}".format(name,h_path,c_path,img))
				elif pat == "y":
					print("NOTE: Your image should contain EXPOSE keyword to use patting")
					mount = input("want to link storage to docker host(y/n): ")
					if mount == "n":
						name = input("Enter your container name: ")
						os.system("docker run -it --name {} -P {}".format(name,img))
					elif mount == "y":
						h_path = input("docker host path: ")
						c_path = input("container path: ")
						name = input("Enter your container name: ")
						os.system("docker run -it --name {} -v {}:{} -P {}".format(name,h_path,c_path,img))
			elif gui == "y":
				pat = input("Want to have patting enabled?(y/n): ")
				if pat == "n":
					mount = input("want to link storage to docker host(y/n): ")
					if mount == "n":
						name = input("Enter your container name: ")
						os.system("docker run -it -e DISPLAY --net=host --name {} {}".format(name,img))
					elif mount == "y":
						h_path = input("docker host path: ")
						c_path = input("container path: ")
						name = input("Enter your container name: ")
						os.system("docker run -it -e DISPLAY --net=host --name {} -v {}:{} {}".format(name,h_path,c_path,img))
				elif pat == "y":
					print("NOTE: Your image should contain EXPOSE keyword to use patting")
					mount = input("want to link storage to docker host(y/n): ")
					if mount == "n":
						name = input("Enter your container name: ")
						os.system("docker run -it -e DISPLAY --net=host --name {} -P {}".format(name,img))
					elif mount == "y":
						h_path = input("docker host path: ")
						c_path = input("container path: ")
						name = input("Enter your container name: ")
						os.system("docker run -it -e DISPLAY --net=host --name {} -P -v {}:{} {}".format(name,h_path,c_path,img))
		elif env == "y":
			env1 = input("Enter environmental variable: ")
			gui = input("Want to run GUI programs(y/n): ")
			if gui == "n":
				pat = input("Want to have patting enabled?(y/n): ")
				if pat == "n":
					mount = input("want to link storage to docker host(y/n): ")
					if mount == "n":
						name = input("Enter your container name: ")
						os.system("docker run -it -e {} --name {} {}".format(env,name,img))
					elif mount == "y":
						h_path = input("docker host path: ")
						c_path = input("container path: ")
						name = input("Enter your container name: ")
						os.system("docker run -it -e {} --name {} -v {}:{}  {}".format(env,name,h_path,c_path,img))
				elif pat == "y":
					print("NOTE: Your image should contain EXPOSE keyword to use patting")
					mount = input("want to link storage to docker host(y/n): ")
					if mount == "n":
						name = input("Enter your container name: ")
						os.system("docker run -it -e {} -P --name {} {}".format(env1,name,img))
					elif mount == "y":
						h_path = input("docker host path: ")
						c_path = input("container path: ")
						name = input("Enter your container name: ")
						os.system("docker run -it -e {} -P --name {} -v {}:{}  {}".format(env1,name,h_path,c_path,img))
			elif gui == "y":
				pat = input("Want to have patting enabled?(y/n): ")
				if pat == "n":
					mount = input("want to link storage to docker host(y/n): ")
					if mount == "n":
						name = input("Enter your container name: ")
						os.system("docker run -it -e {} -e DISPLAY --net=host --name {}  {}".format(env1,name,img))
					elif mount == "y":
						h_path = input("docker host path: ")
						c_path = input("container path: ")
						name = input("Enter your container name: ")
						os.system("docker run -it -e {} -e DISPLAY --net=host --name {} -v {}:{}  {}".format(env1,name,h_path,c_path,img))
				elif pat == "y":
					print("NOTE: Your image should contain EXPOSE keyword to use patting")
					mount = input("want to link storage to docker host(y/n): ")
					if mount == "n":
						name = input("Enter your container name: ")
						os.system("docker run -it -e {} -P -e DISPLAY --net=host --name {} {}".format(env,name,img))
					elif mount == "y":
						h_path = input("docker host path: ")
						c_path = input("container path: ")
						name = input("Enter your container name: ")
						os.system("docker run -it -e {} -P -e DISPLAY --net=host --name {} -v {}:{} {}".format(env,name,h_path,c_path,img))
	elif ch == 7:
		file = input("Enter filename to be copied: ")
		name= input("Enter container name where the file is to be copied: ")
		dest = input("Enter destination path: ")
		os.system("docker cp {} {}:{}".format(file,name,dest))
	

	elif ch == 8:
		os.system("docker ps")


	elif ch == 9:
		os.system("docker ps -a")


	elif ch == 10:
		name = input("Enter your container name/ID: ")
		os.system("docker rm -f {}".format(name))

	elif ch == 11:
		os.system("docker rm -f $(docker ps -a -q)")


	elif ch == 12:
		img = input("Enter image name: ")
		os.system("docker rmi -f {}".format(img))

	elif ch == 13:
		os.system("docker rmi -f $(docker images -a -q)")

	elif ch == 14:
		location = input("Enter new location to create Dockerfile: ")
		os.system("mkdir {}".format(location))
		os.chdir(location)
		img_name =input("Enter image name: ")
		os.system("vim Dockerfile")
		os.system("docker build -t {} {}".format(img_name,os.getcwd()))
		print(os.getcwd())

	elif ch == 15:
		img = input("Image name : ")
		os.system("tput setaf 1")
		print("Note: File name should be provided with '(.tar)' extension")
		os.system("tput setaf 7")
		f_name = input("File name: ")
		os.system("docker save {} -o {}".format(img,f_name))
	
	elif ch == 16:
		f_name = input("File name: ")
		os.system("docker load -i {}".format(f_name))
	
	elif ch == 17:
		c_name = input("Current name: ")
		n_name = input("New name: ")
		os.system("docker tag {} {}".format(c_name,n_name))

	elif ch == 18:
		os.system("tput setaf 1")
		print("""
	Note:Your image should be saved in the below format
			   dockerid/imagename
		""")
		os.system("tput setaf 7")
		img = input("Enter image name: ")
		os.system("docker push {}".format(img))	

	elif ch == 19:
		name = input("Enter conatiner/image name: ")
		os.system("docker inspect {}".format(name))

	elif ch == 20:
		name = input("Enter container name: ")
		os.system("docker start {}".format(name))
		cmd = input("command: ")
		os.system("docker exec {} {}".format(name,cmd))
	
	elif ch == 21:
		os.system("docker network ls")
	
	elif ch == 22:
		net = input("Enter network name: ")
		os.system("docker network inspect {}".format(net))
	elif ch == 23:
		img = input("Enter image name: ")
		os.system("docker history {}".format(img))	
	elif ch == 24:
		break
	input("Press enter to continue........")
	os.system("clear")

