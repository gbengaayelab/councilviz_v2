import jinja2
import os

def main():
    # Define data to pass to the template
    data = {
        'title': 'Council Viz',
        # Add any other data you want to pass to the template here
    }

    # Load the Jinja template from a file
    template_loader = jinja2.FileSystemLoader(searchpath="./views")
    env = jinja2.Environment(loader=template_loader)
    template = env.get_template('committee.html')

    # Render the template with the provided data
    rendered_html = template.render(data)

    # Output or save the rendered HTML
    output_file = os.path.join("views", "rendered_committee.html")
    with open(output_file, 'w') as f:
        f.write(rendered_html)

if __name__ == "__main__":
    main()
