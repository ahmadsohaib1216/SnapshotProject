import boto3
import click

session = boto3.Session(profile_name='sohaib')
ec2 = session.resource('ec2')

@click.command()
def list_all_instances():
	"List Ec2 Instances"
	for i in ec2.instances.all():
		print(i)

if __name__ == '__main__':
list_all_instances()
