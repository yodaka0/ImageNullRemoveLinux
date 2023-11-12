from omegaconf import OmegaConf

from src.runner import Runner
from src.utils.config import RootConfig
import os

# from src.utils.tag import SessionTag

def create_new_structure(src_dir, dst_dir):
    for dir, _ ,_ in os.walk(src_dir):
        dirs_name = dir.replace(dst_dir, "")
        new_dir = dst_dir + "/" + dirs_name.replace("/", "_out/") + "_out"
        os.makedirs(new_dir, exist_ok=True)


cli = OmegaConf.from_cli()  # command line interface config
if cli.get("config_path"):
    cli_conf = OmegaConf.merge(OmegaConf.load(cli.config_path), OmegaConf.from_cli())
else:
    cli_conf = OmegaConf.merge(OmegaConf.load("config/mdet.yaml"), OmegaConf.from_cli())
schema = OmegaConf.structured(
    RootConfig(
        session_root=cli_conf.get("session_root"), output_dir=cli_conf.get("output_dir")
    )
)
session_root=cli_conf.get("session_root")
# print(schema)
# schema = OmegaConf.load("config/mdet.yaml")
config = OmegaConf.merge(schema, cli_conf)

parent_dir = os.path.dirname(session_root)+"/"
create_new_structure(session_root, parent_dir)

runner = Runner(config=config, session_tag="mdet",folders=session_root)
runner.execute()
