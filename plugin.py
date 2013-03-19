###
# Copyright (c) 2004, Jeremiah Fincher
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

'''
Relay data frpom one IRC channel to another. See README.md for
configuration and use
'''


from supybot import callbacks
from supybot import conf
from supybot import ircmsgs
from supybot import log


class RegexRelay(callbacks.Privmsg):
    ''' Main plugin class. '''
    # pylint: disable=E1101,R0904

    def __init__(self, irc):
        callbacks.Privmsg.__init__(self, irc)
        self.log = log.getPluginLogger('regexrelay')

    def shouldRelay(self, msg):
        ''' Dummy docstring. '''
        source = self.registryValue('source')
        if source:
            assert msg.command == 'PRIVMSG'
            return msg.args[0] == source and \
                   bool(self.registryValue('regexp').search(msg.args[1]))
        else:
            return False

    def doPrivmsg(self, irc, msg):
        ''' Dummy docstring. '''
        if self.shouldRelay(msg):
            target = self.registryValue('target')
            if target and target in irc.state.channels:
                if self.registryValue('fancy'):
                    s = ircmsgs.prettyPrint(msg)
                else:
                    s = msg.args[1]
                s = self.registryValue('prefix') + s
                self.log.debug("regexrelay, queuing: " + s)
                irc.queueMsg(ircmsgs.privmsg(target, s))

    def do376(self, irc, msg):
        ''' Dummy docstring. '''
        source = self.registryValue('source')
        target = self.registryValue('target')
        if source and target:
            networkGroup = conf.supybot.networks.get(irc.network)
            irc.queueMsg(networkGroup.channels.join(target))
            irc.queueMsg(networkGroup.channels.join(source))


Class = RegexRelay

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
