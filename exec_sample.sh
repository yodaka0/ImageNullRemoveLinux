python exec_clip.py session_root=/home/dl-node01/MDetToolsForJCameraTraps/_test_dataset/GIFU_WildBoar/R3_Kinkazan_Boar_REST output_dir=/home/dl-node01/MDetToolsForJCameraTraps/_test_dataset/GIFU_WildBoar/R3_Kinkazan_Boar_REST-clip
python exec_mdet.py session_root=/home/dl-node01/MDetToolsForJCameraTraps/_test_dataset/R3_Kinkazan_REST_Boar_Samples
python exec_mdetcrop.py session_root=/home/dl-node01/MDetToolsForJCameraTraps/_test_dataset/R3_Kinkazan_REST_Boar_Samples mdet_result_path=_test_dataset/R3_Kinkazan_REST_Boar_Samples/detector_output.json
python exec_cls.py session_root=/home/dl-node01/MDetToolsForJCameraTraps/_test_dataset/R3_Kinkazan_REST_Boar_Samples-crop
python exec_imgsummary.py session_root=/home/dl-node01/MDetToolsForJCameraTraps/_test_dat