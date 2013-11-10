__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

import pygame


class EventType(object):

    SOUND_PLAYBACK_ENDED = pygame.USEREVENT + 1
    SOUND_PLAY = pygame.USEREVENT + 2
    SOUND_ADD_TO_QUEUE = pygame.USEREVENT + 3
    SOUND_LOOPING_PLAY_WHEN_IDLE = pygame.USEREVENT + 4
    SOUND_PLAY_WHEN_IDLE = pygame.USEREVENT + 5
    SOUND_PLAY_AFTER_DELAY = pygame.USEREVENT + 6
    SOUND_STOP = pygame.USEREVENT + 7
    SOUND_PLAYBACK_ENDED_CHANNEL = pygame.USEREVENT + 8