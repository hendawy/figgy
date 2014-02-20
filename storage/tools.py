# encoding: utf-8
# Created by David Rideout <drideout@safaribooksonline.com> on 2/7/14 4:58 PM
# Copyright (c) 2013 Safari Books Online, LLC. All rights reserved.

from storage.models import Book, Identifier


def process_book_element(book_element):
    """
    Process a book element into the database.

    :param book: book element
    :returns:
    """

    book, created = Book.objects.get_or_create(pk=book_element.get('id'))
    book.title = book_element.findtext('title')
    book.description = book_element.findtext('description')

    for alias in book_element.xpath('aliases/alias'):
        scheme = alias.get('scheme')
        value = alias.get('identifier')

        book.identifiers.get_or_create(scheme=scheme, identifier=value)

    book.save()