###
# Copyright (c) 2005, Jeremiah Fincher
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###

# Unused wildcard imports:
# pylint: disable=W0614,W0401
# Missing docstrings:
# pylint: disable=C0111
# supybot's typenames are irregular
# Too many public methods:
# pylint: disable=R0904


from supybot import conf
from supybot.test import *


class RegexRelayTest(ChannelPluginTestCase):
    plugins = ('RegexRelay',)
    channel = '#test'

    def setUp(self, nick='test'):      # pylint: disable=W0221
        ChannelPluginTestCase.setUp(self)
        conf.supybot.plugins.regexrelay.source.setValue('#test1')
        conf.supybot.plugins.regexrelay.target.setValue('#test')
        conf.supybot.plugins.regexrelay.regexp.set('/git[.]/')

    def testMatch(self):
        self.feedMsg('git.message ivar', to='#test1', frm='test-bot')
        self.assertResponse(' ', '<test-bot> git.message ivar')

    def testNoMatch(self):
        self.feedMsg('got.message ivar', to='#test1', frm='test-bot')
        self.assertResponse('reload regexrelay ',
                            'The operation succeeded.')



# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
