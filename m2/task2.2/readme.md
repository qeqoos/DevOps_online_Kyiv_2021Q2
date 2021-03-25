# Task 2.2


<p>I created Linux Virtual Machine using Amazon Lightsail by following tutorial.</p>

<img src="./screenshots/lightsail.png">

<p>After that, I connected to it using MobaXterm. The key file was downloaded during<br>
the creation of VM. It is used for SSH connection.
</p>

<img src="./screenshots/lightsail2.png">

<p>Next, I created VM using EC2. I chose cent-os and t2.micro instance.<br>
For all VMs, availability zone is <code>eu-central-1a</code> on Frankfurt.
</p>

<img src="./screenshots/secondVM.png">

<p>And also got access for it using MobaXterm.</p>

<img src="./screenshots/secondVM2.png">

<p>To create snapshot, I went to Elastic Block Store -> Snapshots -> Create Snapshot.</p>

<img src="./screenshots/snapshot.png">

<p>I made additional volume for 1GB in the same zone, that I can attach to different VMs.</p>

<p><img src="./screenshots/attach1.png"></p>

<p>For the correct attachment, I used commands:

* <code>sudo mkfs -t xfs /dev/xvdf</code> - creates file system on the volume.
* <code>sudo mkdir /data</code> and <code>sudo mount /dev/xvdf /data</code> - locate volume in data and mount volume.

<p>Put text file <code>file_in_Disk_D</code> into /data:</p>

<img src="./screenshots/attach2.png">

<p>I created new VM using the image from snapshot.</p>

<img src="./screenshots/from-backup1.png">

<img src="./screenshots/from-backup2.png">

<p>I deattached Disk_D, and attached it to new instance:</p>

<img src="./screenshots/reattach1.png">

<p>Mount is required, so I do <code>sudo mkdir /newdata</code> and <code>sudo mount /dev/xvdf /newdata</code>.</p>

<img src="./screenshots/reattach2.png">

<p>As we see, file <code>file_in_Disk_D</code> moved here with volume.</p>

<p>Next, I created WordPress instance and accessed it through terminal.<br>
To log into Wordpress Admin Page, I need bitnami password. It is located in:
<code>$HOME/bitnami_application_password</code>
</p>

<img src="./screenshots/wordpress1.png">

<p>Here I successfully logged to administration dashboard, where I can manage my page.</p>

<img src="./screenshots/wordpress2.png">

<p>Next, I created S3 bucket to be able to store and download files from this storage.</p>

<img src="./screenshots/s3_1.png">

<p>Here, I uploaded file to S3, and now have opportunity to retrieve it.</p>

<img src="./screenshots/s3_3.png">

<p>I created IAM user Pavel_Admin with Programmatic access and AdministratorAccess.<br>
Downloaded .csv file with credentials.
</p>

<img src="./screenshots/iam_1.png">

<p>In order to use AWS CLI, I installed AWSCLI and configured it with <code>aws configure</code>.<br>
I entered corresponding information into cmd.
</p>

<img src="./screenshots/iam_2.png">

<p>Different commands were used for uploading, copying and deleting object on S3 through Windows CMD.</p>

<img src="./screenshots/iam_3.png">

<p>I deployed Docker Containers on Amazon Elastic Container Service (ECS).</p>

<img src="./screenshots/cluster1.png">

<p>Online demo application of working cluster.</p>

<img src="./screenshots/cluster2.png">

<p>Next, new S3 bucket was created. It will contain HTML page and all materials used for it.</p>

<img src="./screenshots/15_1.png">

<p>To upload necessary files, I executed next commands:</p>

<img src="./screenshots/15_3.png">

<p>Now, I enable static web hosting for my bucket and specified default page for it:</p>

<img src="./screenshots/15_2.png">

<p>In order for people to be able to access my webpage, I edited access settings and disabled blocking of public access.<br>
It is also necessary to edit bucket policy. I created JSON with required template, and pasted it to <code>bucket policy</code> field.
</p>

<img src="./screenshots/15_4.png">

<p>Here you can access my webpage using this URL: <a href="http://pavel-webbucket.s3-website.eu-central-1.amazonaws.com">click here</a></p>

<img src="./screenshots/15_5.png">