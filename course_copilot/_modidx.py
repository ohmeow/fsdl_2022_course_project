# Autogenerated by nbdev

d = { 'settings': { 'branch': 'master',
                'doc_baseurl': '/course_copilot',
                'doc_host': 'https://ohmeow.github.io',
                'git_url': 'https://github.com/ohmeow/fsdl_2022_course_project',
                'lib_path': 'course_copilot'},
  'syms': { 'course_copilot.preprocessing': { 'course_copilot.preprocessing.build_segmentation_train_df': ( 'preprocessing.html#build_segmentation_train_df',
                                                                                                            'course_copilot/preprocessing.py'),
                                              'course_copilot.preprocessing.build_summarization_train_df': ( 'preprocessing.html#build_summarization_train_df',
                                                                                                             'course_copilot/preprocessing.py'),
                                              'course_copilot.preprocessing.build_train_df': ( 'preprocessing.html#build_train_df',
                                                                                               'course_copilot/preprocessing.py'),
                                              'course_copilot.preprocessing.convert_duration_to_seconds': ( 'preprocessing.html#convert_duration_to_seconds',
                                                                                                            'course_copilot/preprocessing.py'),
                                              'course_copilot.preprocessing.preprocess_data': ( 'preprocessing.html#preprocess_data',
                                                                                                'course_copilot/preprocessing.py')},
            'course_copilot.summarization': { 'course_copilot.summarization.ContentSummarizationConfig': ( 'summarization.html#contentsummarizationconfig',
                                                                                                           'course_copilot/summarization.py'),
                                              'course_copilot.summarization.HeadlineSummarizationConfig': ( 'summarization.html#headlinesummarizationconfig',
                                                                                                            'course_copilot/summarization.py'),
                                              'course_copilot.summarization.SummarizationConfig': ( 'summarization.html#summarizationconfig',
                                                                                                    'course_copilot/summarization.py'),
                                              'course_copilot.summarization.SummarizationModelTrainer': ( 'summarization.html#summarizationmodeltrainer',
                                                                                                          'course_copilot/summarization.py'),
                                              'course_copilot.summarization.SummarizationModelTrainer.__init__': ( 'summarization.html#summarizationmodeltrainer.__init__',
                                                                                                                   'course_copilot/summarization.py'),
                                              'course_copilot.summarization.SummarizationModelTrainer.get_preds': ( 'summarization.html#summarizationmodeltrainer.get_preds',
                                                                                                                    'course_copilot/summarization.py'),
                                              'course_copilot.summarization.SummarizationModelTrainer.get_training_data': ( 'summarization.html#summarizationmodeltrainer.get_training_data',
                                                                                                                            'course_copilot/summarization.py'),
                                              'course_copilot.summarization.SummarizationModelTrainer.load_learner_or_model': ( 'summarization.html#summarizationmodeltrainer.load_learner_or_model',
                                                                                                                                'course_copilot/summarization.py'),
                                              'course_copilot.summarization.SummarizationModelTrainer.train': ( 'summarization.html#summarizationmodeltrainer.train',
                                                                                                                'course_copilot/summarization.py'),
                                              'course_copilot.summarization._get_dls': ( 'summarization.html#_get_dls',
                                                                                         'course_copilot/summarization.py'),
                                              'course_copilot.summarization._get_learner': ( 'summarization.html#_get_learner',
                                                                                             'course_copilot/summarization.py'),
                                              'course_copilot.summarization._get_preds': ( 'summarization.html#_get_preds',
                                                                                           'course_copilot/summarization.py'),
                                              'course_copilot.summarization._get_task_hf_objects': ( 'summarization.html#_get_task_hf_objects',
                                                                                                     'course_copilot/summarization.py'),
                                              'course_copilot.summarization._get_training_data': ( 'summarization.html#_get_training_data',
                                                                                                   'course_copilot/summarization.py')},
            'course_copilot.tasks': { 'course_copilot.tasks.add_required_args': ('tasks.html#add_required_args', 'course_copilot/tasks.py'),
                                      'course_copilot.tasks.build_train_config': ( 'tasks.html#build_train_config',
                                                                                   'course_copilot/tasks.py'),
                                      'course_copilot.tasks.prepare_tuning': ('tasks.html#prepare_tuning', 'course_copilot/tasks.py'),
                                      'course_copilot.tasks.run_experiment': ('tasks.html#run_experiment', 'course_copilot/tasks.py')},
            'course_copilot.topic_segmentation': { 'course_copilot.topic_segmentation.MarginRankingLoss': ( 'topic_segmentation.html#marginrankingloss',
                                                                                                            'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.SiameseBatchTokenizeTransform': ( 'topic_segmentation.html#siamesebatchtokenizetransform',
                                                                                                                        'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.SiameseBatchTokenizeTransform.__init__': ( 'topic_segmentation.html#siamesebatchtokenizetransform.__init__',
                                                                                                                                 'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.SiameseBatchTokenizeTransform.encodes': ( 'topic_segmentation.html#siamesebatchtokenizetransform.encodes',
                                                                                                                                'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.TopicSegmentationConfig': ( 'topic_segmentation.html#topicsegmentationconfig',
                                                                                                                  'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.TopicSegmentationModelTrainer': ( 'topic_segmentation.html#topicsegmentationmodeltrainer',
                                                                                                                        'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.TopicSegmentationModelTrainer.__init__': ( 'topic_segmentation.html#topicsegmentationmodeltrainer.__init__',
                                                                                                                                 'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.TopicSegmentationModelTrainer.get_preds': ( 'topic_segmentation.html#topicsegmentationmodeltrainer.get_preds',
                                                                                                                                  'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.TopicSegmentationModelTrainer.get_training_data': ( 'topic_segmentation.html#topicsegmentationmodeltrainer.get_training_data',
                                                                                                                                          'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.TopicSegmentationModelTrainer.load_learner_or_model': ( 'topic_segmentation.html#topicsegmentationmodeltrainer.load_learner_or_model',
                                                                                                                                              'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.TopicSegmentationModelTrainer.train': ( 'topic_segmentation.html#topicsegmentationmodeltrainer.train',
                                                                                                                              'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.TopicSegmentationModelWrapper': ( 'topic_segmentation.html#topicsegmentationmodelwrapper',
                                                                                                                        'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.TopicSegmentationModelWrapper.__init__': ( 'topic_segmentation.html#topicsegmentationmodelwrapper.__init__',
                                                                                                                                 'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.TopicSegmentationModelWrapper.forward': ( 'topic_segmentation.html#topicsegmentationmodelwrapper.forward',
                                                                                                                                'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation._build_neg_inputs': ( 'topic_segmentation.html#_build_neg_inputs',
                                                                                                            'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation._build_pos_inputs': ( 'topic_segmentation.html#_build_pos_inputs',
                                                                                                            'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation._build_targets': ( 'topic_segmentation.html#_build_targets',
                                                                                                         'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation._get_dls': ( 'topic_segmentation.html#_get_dls',
                                                                                                   'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation._get_learner': ( 'topic_segmentation.html#_get_learner',
                                                                                                       'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation._get_preds': ( 'topic_segmentation.html#_get_preds',
                                                                                                     'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation._get_task_hf_objects': ( 'topic_segmentation.html#_get_task_hf_objects',
                                                                                                               'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation._get_training_data': ( 'topic_segmentation.html#_get_training_data',
                                                                                                             'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation._get_validation_preds': ( 'topic_segmentation.html#_get_validation_preds',
                                                                                                                'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.blurr_splitter_on_backbone': ( 'topic_segmentation.html#blurr_splitter_on_backbone',
                                                                                                                     'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.blurr_splitter_with_head': ( 'topic_segmentation.html#blurr_splitter_with_head',
                                                                                                                   'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.depth_score_cal': ( 'topic_segmentation.html#depth_score_cal',
                                                                                                          'course_copilot/topic_segmentation.py'),
                                                   'course_copilot.topic_segmentation.topic_seg_f1_score': ( 'topic_segmentation.html#topic_seg_f1_score',
                                                                                                             'course_copilot/topic_segmentation.py')},
            'course_copilot.training': { 'course_copilot.training.ModelTrainer': ( 'training.html#modeltrainer',
                                                                                   'course_copilot/training.py'),
                                         'course_copilot.training.ModelTrainer.__init__': ( 'training.html#modeltrainer.__init__',
                                                                                            'course_copilot/training.py'),
                                         'course_copilot.training.ModelTrainer.configure_sweep': ( 'training.html#modeltrainer.configure_sweep',
                                                                                                   'course_copilot/training.py'),
                                         'course_copilot.training.ModelTrainer.get_preds': ( 'training.html#modeltrainer.get_preds',
                                                                                             'course_copilot/training.py'),
                                         'course_copilot.training.ModelTrainer.get_train_config_props': ( 'training.html#modeltrainer.get_train_config_props',
                                                                                                          'course_copilot/training.py'),
                                         'course_copilot.training.ModelTrainer.get_training_data': ( 'training.html#modeltrainer.get_training_data',
                                                                                                     'course_copilot/training.py'),
                                         'course_copilot.training.ModelTrainer.init_wandb_run': ( 'training.html#modeltrainer.init_wandb_run',
                                                                                                  'course_copilot/training.py'),
                                         'course_copilot.training.ModelTrainer.load_learner_or_model': ( 'training.html#modeltrainer.load_learner_or_model',
                                                                                                         'course_copilot/training.py'),
                                         'course_copilot.training.ModelTrainer.train': ( 'training.html#modeltrainer.train',
                                                                                         'course_copilot/training.py'),
                                         'course_copilot.training.ModelTrainer.update_train_config_from_sweep_params': ( 'training.html#modeltrainer.update_train_config_from_sweep_params',
                                                                                                                         'course_copilot/training.py'),
                                         'course_copilot.training.TrainConfig': ('training.html#trainconfig', 'course_copilot/training.py'),
                                         'course_copilot.training.get_train_config_props': ( 'training.html#get_train_config_props',
                                                                                             'course_copilot/training.py')},
            'course_copilot.transcription': { 'course_copilot.transcription.fetch_transcription': ( 'transcription.html#fetch_transcription',
                                                                                                    'course_copilot/transcription.py'),
                                              'course_copilot.transcription.fetch_youtube_audio': ( 'transcription.html#fetch_youtube_audio',
                                                                                                    'course_copilot/transcription.py'),
                                              'course_copilot.transcription.transcription_to_df': ( 'transcription.html#transcription_to_df',
                                                                                                    'course_copilot/transcription.py')},
            'course_copilot.utils': { 'course_copilot.utils.detect_env': ('utils.html#detect_env', 'course_copilot/utils.py'),
                                      'course_copilot.utils.print_dev_environment': ( 'utils.html#print_dev_environment',
                                                                                      'course_copilot/utils.py')}}}