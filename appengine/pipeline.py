"""
pipeline
"""
from mapreduce import base_handler
from mapreduce import mapreduce_pipeline

class ClassifierTrainingPipeline(base_handler.PipelineBase):
	"""
	the pipeline to train classifier
	"""
	def run(self, shards):
	    yield mapreduce_pipeline.MapperPipeline(
            "Mention Export",
            "steprep.domain.export_to_core.mentionToJson",
            "mapreduce.input_readers.DatastoreInputReader",
            output_writer_spec="mapreduce.output_writers.FileOutputWriter",
            params={
                "input_reader" : {
                    "entity_kind": "steprep.api.models.account_entry.AccountEntry",
                    "namespace":   "",
                },
                "output_writer" : {
                    "filesystem": "gs",
                    "gs_bucket_name": BUCKET_NAME,
                    "output_sharding": "input",
                },
            },
            shards=shards
        )