# dbMain_test.py

import logging
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .queries import (
	create_test_entry,
	get_all_test_entries,
	get_test_entry_by_id,
	delete_test_entry_by_id  # Add this line to import the function
)
from .models import TestEntry
from .db_utils import insert_into_table
from .db_connection import db_connection

# Get an instance of a logger
logger = logging.getLogger('cleartask')

@method_decorator(csrf_exempt, name='dispatch')
class InsertTestView(View):
    def post(self, request):
        logger.debug('InsertTestView POST request received')
        try:
            data = json.loads(request.body)
            logger.debug(f'Request data: {data}')
            name = data.get('name')
            description = data.get('description')
            if not name or not description:
                logger.error('Invalid data: name or description missing')
                return JsonResponse({'error': 'Invalid data'}, status=400)
            
            # Use the existing database connection
            if db_connection is None:
                return JsonResponse({'error': 'Database connection failed'}, status=500)
            
            # Fetch the maximum id value from the table
            cursor = db_connection.cursor()
            cursor.execute("SELECT COALESCE(MAX(id), 0) FROM test_entries")
            max_id = cursor.fetchone()[0]
            new_id = max_id + 1
            cursor.close()
            
            # Insert data into the table with the new id
            insert_into_table(db_connection, 'test_entries', {'id': new_id, 'name': name, 'description': description})
            logger.info('Data inserted successfully')
            return JsonResponse({'id': new_id, 'name': name, 'description': description}, status=201)
        except json.JSONDecodeError:
            logger.error('Invalid JSON')
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            logger.error(f'Unexpected error: {e}')
            return JsonResponse({'error': 'Internal server error'}, status=500)

class GetTestView(View):
	def get(self, request):
		try:
			test_entries = get_all_test_entries().values('id', 'name', 'description')
			logger.info('Fetched all test entries')
			return JsonResponse(list(test_entries), safe=False)
		except Exception as e:
			logger.error(f'Unexpected error: {e}')
			return JsonResponse({'error': 'Internal server error'}, status=500)

class GetTestDetailView(View):
	def get(self, request, pk):
		try:
			test_entry = get_test_entry_by_id(pk)
			logger.info(f'Fetched test entry: {test_entry.id}')
			return JsonResponse({'id': test_entry.id, 'name': test_entry.name, 'description': test_entry.description})
		except TestEntry.DoesNotExist:
			logger.error(f'Test entry not found: {pk}')
			return JsonResponse({'error': 'Test entry not found'}, status=404)
		except Exception as e:
			logger.error(f'Unexpected error: {e}')
			return JsonResponse({'error': 'Internal server error'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class DeleteTestView(View):
	def delete(self, request, pk):
		try:
			delete_test_entry_by_id(pk)
			logger.info(f'Deleted test entry: {pk}')
			return JsonResponse({}, status=204)
		except TestEntry.DoesNotExist:
			logger.error(f'Test entry not found: {pk}')
			return JsonResponse({'error': 'Test entry not found'}, status=404)
		except Exception as e:
			logger.error(f'Unexpected error: {e}')
			return JsonResponse({'error': 'Internal server error'}, status=500)