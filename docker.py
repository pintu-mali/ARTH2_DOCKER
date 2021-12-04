import os


print("""
############################################
#                                          #
#           hello                          #
#                                          #
#                                          #
############################################

____________________________________________
____________________________________________
""")

while True:
	print("""
	Press 1	: To install docker
	Press 2	: To start docker services
	Press 3	: To download docker images
	Press 4	: To launch docker container
	Press 5	: To check running containers
	Press 6	: To see all containers
	Press 7	: To delete a container
	Press 8	: To delete all the containers
	Press 9	: To delete any image
	Press 10: To delete all the images
	Press 11: To create an image
	Press 12: For main menu
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
		img = input("Enter image name: ")
		os.system("docker pull {}".format(img))

	elif ch == 4:
		img =input("Enter image name:")
		env =input("Want any environmental variable(y/n): ")
		if env == "n":
			gui =input("Want to run GUI programs(y/n): ")
			if gui == "n":
				pat = input("Want to have patting enabled?(y/n): ")
				if pat == "n":
					name = input("Enter your container name: ")
					os.system("docker run -it --name {} {}".format(name,img))
				elif pat == "y":
					print("NOTE: Your image should contain EXPOSE keyword to use patting")
					name = input("Enter your container name: ")
					os.system("docker run -it --name {} -P {}".format(name,img))
			elif gui == "y":
				pat = input("Want to have patting enabled?(y/n): ")
				if pat == "n":
					name = input("Enter your container name: ")
					os.system("docker run -it -e DISPLAY --net=host --name {} {}".format(name,img))
				elif pat == "y":
					print("NOTE: Your image should contain EXPOSE keyword to use patting")
					name = input("Enter your container name: ")
					os.system("docker run -it -e DISPLAY --net=host --name {} -P {}".format(name,img))
		elif env == "y":
			env1 = input("Enter environmental variable: ")
			gui = input("Want to run GUI programs(y/n): ")
			if gui == "n":
				pat = input("Want to have patting enabled?(y/n): ")
				if pat == "n":
					name = input("Enter your container name: ")
					os.system("docker run -it -e {} --name {} {}".format(env,name,img))
				elif pat == "y":
					print("NOTE: Your image should contain EXPOSE keyword to use patting")
					name = input("Enter your container name: ")
					os.system("docker run -it -e {} -P --name {} {}".format(env1,name,img))
			elif gui == "y":
				pat = input("Want to have patting enabled?(y/n): ")
				if pat == "n":
					name = input("Enter your container name: ")
					os.system("docker run -it -e {} -e DISPLAY --net=host --name {}  {}".format(env1,name,img))
				elif pat == "y":
					print("NOTE: Your image should contain EXPOSE keyword to use patting")
					name = input("Enter your container name: ")
					os.system("docker run -it -e {} -P -e DISPLAY --net=host --name {} {}".format(env,name,img))

	elif ch == 5:
		os.system("docker ps")


	elif ch == 6:
		os.system("docker ps -a")


	elif ch == 7:
		name = input("Enter your container name/ID: ")
		os.system("docker rm -f {}".format(name))

	elif ch == 8:
		os.system("docker rm -f $(docker ps -a -q)")


	elif ch == 9:
		img = input("Enter image name: ")
		os.system("docker rmi -f {}".format(img))

	elif ch == 10:
		os.system("docker rmi -f $(docker images -a -q)")

	elif ch == 11:
		location = input("Enter new location to create Dockerfile: ")
		os.system("mkdir {}".format(location))
		os.chdir(location)
		img_name =input("Enter image name: ")
		os.system("vim Dockerfile")
		os.system("docker build -t {} {}".format(img_name,os.getcwd()))
		print(os.getcwd())
	elif ch == 12:
		break
	input("Press enter to continue........")
	os.system("clear")
