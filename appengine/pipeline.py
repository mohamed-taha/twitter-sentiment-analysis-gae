"""
pipeline
"""
from mapreduce import base_handler
from mapreduce import mapreduce_pipeline

def entry_map(entity):
    """
    convert entity into list
    """
    return entity

def entry_reduce(key, value):
    pass

class ClassifierTrainingPipeline(base_handler.PipelineBase):
	"""
	the pipeline to train classifier
	"""
	def run(self, shards):
	    yield mapreduce_pipeline.MapperPipeline(
            "Train Classifier",
            "pipeline.entry_map",
            "pipeline.entry_reduce",
            "mapreduce.input_readers.DatastoreInputReader",
            output_writer_spec="mapreduce.output_writers.BlobstoreOutputWriter",
            mapper_params={
                "input_reader" : {
                    "entity_kind": "steprep.api.models.account_entry.AccountEntry",
                    "namespace":   "",
                }},
            reducer_params={"mime_type": "text/plain",},
            shards=shards
        )