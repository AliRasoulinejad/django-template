from config.env import env
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

DjangoInstrumentor().instrument()
Psycopg2Instrumentor().instrument()
LoggingInstrumentor().instrument()

jaeger_exporter = JaegerExporter(
    agent_host_name=env.str("JAEGER_HOST"),
    agent_port=env.int("JAEGER_PORT"),
)
trace.set_tracer_provider(TracerProvider(
    resource=Resource.create({SERVICE_NAME: '{{cookiecutter.project_slug}}'})
))
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
