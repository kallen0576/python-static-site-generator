import typer
from ssg.site import Site 




#if __name__ == "___main__"():
def main(source = "content",dest = "dist"):
        config = {"source": "source",'dest': 'dist'}
        Site(**config).build()

typer.run(main)