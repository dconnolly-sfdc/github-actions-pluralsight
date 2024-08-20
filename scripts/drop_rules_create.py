'''Script to generate terraform file with drop rules for an application, based on application name as input'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--application_name', required=True, help='name of non compliant application')

args = parser.parse_args()

# Define the variables to substitute
variables = {
    'application_name': args.application_name
}
# Define the template and output file paths
template_file = 'scripts/drop_rules_template.tf'
output_file = f'non-compliant-applications/drop_rule_{variables["application_name"].strip()}.tf'

# Read the template file
with open(template_file, 'r') as file:
    template_content = file.read()
    # Substitute the variables in the template
    populated_content = template_content
    for key, value in variables.items():
        populated_content = populated_content.replace(f'{{{{{key}}}}}', value)
        # Write the populated content to the output file
    with open(output_file, 'w') as file:
        file.write(populated_content)
        print(f'Template populated and saved to {output_file}')
