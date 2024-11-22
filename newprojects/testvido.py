mydata = {
    'item': [{
            'metadata': {
                'revision': 'VX-369,VX-355,VX-342,VX-358,VX-345',
                'group': [],
                'timespan': [{
                        'field': [],
                        'group': [{
                                'name': 'vod_movie',
                                'id': [],
                                'field': [{
                                        'name': 'vod_title',
                                        'id': [],
                                        'value': [{
                                                'value': 'Toy Story 4',
                                                'uuid': 'cd40b8af-47dd-47c0-9f71-2f110d596b2f',
                                                'user': 'admin',
                                                'timestamp': '2019-09-14T13:26:12.795+0000',
                                                'change': 'VX-339'
                                            }
                                        ],
                                        'data': [],
                                        'uuid': '0c58ae7c-fa2a-4906-8f17-92e122bacc4a',
                                        'user': 'admin',
                                        'timestamp': '2019-09-14T13:26:12.795+0000',
                                        'change': 'VX-339'
                                    }
                                ],
                                'group': [],
                                'data': [],
                                'inheritance': 'Collection/VX-88',
                                'uuid': '90ab75b7-4d90-4b87-86a0-bc1725538da4',
                                'user': 'admin',
                                'timestamp': '2019-09-14T13:26:12.795+0000',
                                'change': 'VX-339'
                            }
                        ],
                        'start': '-INF',
                        'end': '+INF'
                    }
                ]
            },
            'id': 'VX-37'
        }
    ]
}


print(mydata['item'][0])