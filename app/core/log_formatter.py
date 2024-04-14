import json
import logging

import logstash


class LogstashFormatter(logstash.formatter.LogstashFormatterVersion0):
    """Helper class for formatting for Logstash"""

    @classmethod
    def serialize(cls, message):
        """Serialize the message

        Args:
            message: the message you want to serialize

        Returns:
            JSON dump of the message
        """
        return json.dumps(message)


class DatadogFormatter(logstash.formatter.LogstashFormatterBase):
    """Helper class for formatting for DataDag"""

    def format(self, record: logging.LogRecord):
        """format a record for datadog

        Args:
            record (logging.LogRecord): Record you want to log

        Returns:
            serialized version of the message
        """

        fields_entry = "@fields"

        # Create message dict
        message = {
            "@timestamp": self.format_timestamp(record.created),
            "@message": record.getMessage(),
            "@source": self.format_source(
                self.message_type, self.host, record.pathname
            ),
            "@source_host": self.host,
            "@source_path": record.pathname,
            "@tags": self.tags,
            "@type": self.message_type,
            "@severity": record.levelname,
            fields_entry: {"logger": record.name},
        }

        # Add extra fields
        self.add_fields(record, fields_entry)

        # If exception, add debug info
        self.add_exception(record, fields_entry)

        return self.serialize(message)

    def add_fields(self, record, field):
        """Add field to record

        Args:
            record: record you want to add field to
            field: Field you want to add
        """
        self.message[field].update(self.get_extra_fields(record))

    def add_exception(self, record, field):
        """Add exception to record

        Args:
            record: record you want to add exception to
            field: Field
        """
        if record.exc_info:
            self.message[field].update(self.get_debug_fields(record))

    @classmethod
    def serialize(cls, message):
        """Serialize the message

        Args:
            message: the message you want to serialize

        Returns:
            JSON dump of the message
        """
        return json.dumps(message)
