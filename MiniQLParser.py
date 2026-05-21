# Generated from C:/Users/ASUS/OneDrive/Desktop/lenguajes-programacion/miniQL/MiniQL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,41,8,3,
        1,4,1,4,1,4,1,4,3,4,47,8,4,1,5,1,5,1,6,1,6,1,6,1,6,5,6,55,8,6,10,
        6,12,6,58,9,6,3,6,60,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,70,
        8,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,78,8,7,10,7,12,7,81,9,7,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,3,9,90,8,9,1,9,0,1,14,10,0,2,4,6,8,10,12,14,
        16,18,0,2,1,0,6,7,1,0,12,17,95,0,21,1,0,0,0,2,31,1,0,0,0,4,33,1,
        0,0,0,6,36,1,0,0,0,8,42,1,0,0,0,10,48,1,0,0,0,12,59,1,0,0,0,14,69,
        1,0,0,0,16,82,1,0,0,0,18,89,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,
        22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,5,
        0,0,1,26,1,1,0,0,0,27,32,3,4,2,0,28,32,3,6,3,0,29,32,3,8,4,0,30,
        32,3,10,5,0,31,27,1,0,0,0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,1,0,
        0,0,32,3,1,0,0,0,33,34,5,1,0,0,34,35,5,22,0,0,35,5,1,0,0,0,36,37,
        5,2,0,0,37,40,3,12,6,0,38,39,5,3,0,0,39,41,3,14,7,0,40,38,1,0,0,
        0,40,41,1,0,0,0,41,7,1,0,0,0,42,43,5,4,0,0,43,44,5,5,0,0,44,46,5,
        24,0,0,45,47,7,0,0,0,46,45,1,0,0,0,46,47,1,0,0,0,47,9,1,0,0,0,48,
        49,5,8,0,0,49,11,1,0,0,0,50,60,5,19,0,0,51,56,5,24,0,0,52,53,5,18,
        0,0,53,55,5,24,0,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,
        57,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,59,50,1,0,0,0,59,51,1,0,0,
        0,60,13,1,0,0,0,61,62,6,7,-1,0,62,63,5,11,0,0,63,70,3,14,7,3,64,
        65,5,20,0,0,65,66,3,14,7,0,66,67,5,21,0,0,67,70,1,0,0,0,68,70,3,
        16,8,0,69,61,1,0,0,0,69,64,1,0,0,0,69,68,1,0,0,0,70,79,1,0,0,0,71,
        72,10,5,0,0,72,73,5,10,0,0,73,78,3,14,7,6,74,75,10,4,0,0,75,76,5,
        9,0,0,76,78,3,14,7,5,77,71,1,0,0,0,77,74,1,0,0,0,78,81,1,0,0,0,79,
        77,1,0,0,0,79,80,1,0,0,0,80,15,1,0,0,0,81,79,1,0,0,0,82,83,5,24,
        0,0,83,84,7,1,0,0,84,85,3,18,9,0,85,17,1,0,0,0,86,90,5,22,0,0,87,
        90,5,23,0,0,88,90,5,24,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,1,0,
        0,0,90,19,1,0,0,0,10,23,31,40,46,56,59,69,77,79,89
    ]

class MiniQLParser ( Parser ):

    grammarFileName = "MiniQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'LOAD'", "'SELECT'", "'WHERE'", "'SORT'", 
                     "'BY'", "'ASC'", "'DESC'", "'SHOW'", "'AND'", "'OR'", 
                     "'NOT'", "'='", "'!='", "'<='", "'>='", "'<'", "'>'", 
                     "','", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "LOAD", "SELECT", "WHERE", "SORT", "BY", 
                      "ASC", "DESC", "SHOW", "AND", "OR", "NOT", "EQ", "NEQ", 
                      "LTE", "GTE", "LT", "GT", "COMMA", "STAR", "LPAREN", 
                      "RPAREN", "STRING", "NUMBER", "ID", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_loadStmt = 2
    RULE_selectStmt = 3
    RULE_sortStmt = 4
    RULE_showStmt = 5
    RULE_columns = 6
    RULE_condition = 7
    RULE_comparison = 8
    RULE_value = 9

    ruleNames =  [ "program", "statement", "loadStmt", "selectStmt", "sortStmt", 
                   "showStmt", "columns", "condition", "comparison", "value" ]

    EOF = Token.EOF
    LOAD=1
    SELECT=2
    WHERE=3
    SORT=4
    BY=5
    ASC=6
    DESC=7
    SHOW=8
    AND=9
    OR=10
    NOT=11
    EQ=12
    NEQ=13
    LTE=14
    GTE=15
    LT=16
    GT=17
    COMMA=18
    STAR=19
    LPAREN=20
    RPAREN=21
    STRING=22
    NUMBER=23
    ID=24
    WS=25
    COMMENT=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniQLParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniQLParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniQLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniQLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 278) != 0)):
                    break

            self.state = 25
            self.match(MiniQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniQLParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SelectStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def selectStmt(self):
            return self.getTypedRuleContext(MiniQLParser.SelectStmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStatement" ):
                return visitor.visitSelectStatement(self)
            else:
                return visitor.visitChildren(self)


    class LoadStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def loadStmt(self):
            return self.getTypedRuleContext(MiniQLParser.LoadStmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStatement" ):
                return visitor.visitLoadStatement(self)
            else:
                return visitor.visitChildren(self)


    class SortStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sortStmt(self):
            return self.getTypedRuleContext(MiniQLParser.SortStmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSortStatement" ):
                return visitor.visitSortStatement(self)
            else:
                return visitor.visitChildren(self)


    class ShowStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def showStmt(self):
            return self.getTypedRuleContext(MiniQLParser.ShowStmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowStatement" ):
                return visitor.visitShowStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MiniQLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = MiniQLParser.LoadStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.loadStmt()
                pass
            elif token in [2]:
                localctx = MiniQLParser.SelectStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.selectStmt()
                pass
            elif token in [4]:
                localctx = MiniQLParser.SortStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.sortStmt()
                pass
            elif token in [8]:
                localctx = MiniQLParser.ShowStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.showStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(MiniQLParser.LOAD, 0)

        def STRING(self):
            return self.getToken(MiniQLParser.STRING, 0)

        def getRuleIndex(self):
            return MiniQLParser.RULE_loadStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStmt" ):
                return visitor.visitLoadStmt(self)
            else:
                return visitor.visitChildren(self)




    def loadStmt(self):

        localctx = MiniQLParser.LoadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(MiniQLParser.LOAD)
            self.state = 34
            self.match(MiniQLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(MiniQLParser.SELECT, 0)

        def columns(self):
            return self.getTypedRuleContext(MiniQLParser.ColumnsContext,0)


        def WHERE(self):
            return self.getToken(MiniQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return MiniQLParser.RULE_selectStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStmt" ):
                return visitor.visitSelectStmt(self)
            else:
                return visitor.visitChildren(self)




    def selectStmt(self):

        localctx = MiniQLParser.SelectStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_selectStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(MiniQLParser.SELECT)
            self.state = 37
            self.columns()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 38
                self.match(MiniQLParser.WHERE)
                self.state = 39
                self.condition(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SortStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.direction = None # Token

        def SORT(self):
            return self.getToken(MiniQLParser.SORT, 0)

        def BY(self):
            return self.getToken(MiniQLParser.BY, 0)

        def ID(self):
            return self.getToken(MiniQLParser.ID, 0)

        def ASC(self):
            return self.getToken(MiniQLParser.ASC, 0)

        def DESC(self):
            return self.getToken(MiniQLParser.DESC, 0)

        def getRuleIndex(self):
            return MiniQLParser.RULE_sortStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSortStmt" ):
                return visitor.visitSortStmt(self)
            else:
                return visitor.visitChildren(self)




    def sortStmt(self):

        localctx = MiniQLParser.SortStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sortStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MiniQLParser.SORT)
            self.state = 43
            self.match(MiniQLParser.BY)
            self.state = 44
            self.match(MiniQLParser.ID)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 45
                localctx.direction = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx.direction = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOW(self):
            return self.getToken(MiniQLParser.SHOW, 0)

        def getRuleIndex(self):
            return MiniQLParser.RULE_showStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowStmt" ):
                return visitor.visitShowStmt(self)
            else:
                return visitor.visitChildren(self)




    def showStmt(self):

        localctx = MiniQLParser.ShowStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_showStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MiniQLParser.SHOW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniQLParser.RULE_columns

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NamedColumnsContext(ColumnsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.ColumnsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniQLParser.ID)
            else:
                return self.getToken(MiniQLParser.ID, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniQLParser.COMMA)
            else:
                return self.getToken(MiniQLParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedColumns" ):
                return visitor.visitNamedColumns(self)
            else:
                return visitor.visitChildren(self)


    class AllColumnsContext(ColumnsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.ColumnsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STAR(self):
            return self.getToken(MiniQLParser.STAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllColumns" ):
                return visitor.visitAllColumns(self)
            else:
                return visitor.visitChildren(self)



    def columns(self):

        localctx = MiniQLParser.ColumnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = MiniQLParser.AllColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(MiniQLParser.STAR)
                pass
            elif token in [24]:
                localctx = MiniQLParser.NamedColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(MiniQLParser.ID)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 52
                    self.match(MiniQLParser.COMMA)
                    self.state = 53
                    self.match(MiniQLParser.ID)
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniQLParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OrCondContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniQLParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MiniQLParser.ConditionContext,i)

        def OR(self):
            return self.getToken(MiniQLParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrCond" ):
                return visitor.visitOrCond(self)
            else:
                return visitor.visitChildren(self)


    class AndCondContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniQLParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MiniQLParser.ConditionContext,i)

        def AND(self):
            return self.getToken(MiniQLParser.AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndCond" ):
                return visitor.visitAndCond(self)
            else:
                return visitor.visitChildren(self)


    class NotCondContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MiniQLParser.NOT, 0)
        def condition(self):
            return self.getTypedRuleContext(MiniQLParser.ConditionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotCond" ):
                return visitor.visitNotCond(self)
            else:
                return visitor.visitChildren(self)


    class CompCondContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparison(self):
            return self.getTypedRuleContext(MiniQLParser.ComparisonContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompCond" ):
                return visitor.visitCompCond(self)
            else:
                return visitor.visitChildren(self)


    class ParenCondContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniQLParser.LPAREN, 0)
        def condition(self):
            return self.getTypedRuleContext(MiniQLParser.ConditionContext,0)

        def RPAREN(self):
            return self.getToken(MiniQLParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenCond" ):
                return visitor.visitParenCond(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniQLParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = MiniQLParser.NotCondContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 62
                self.match(MiniQLParser.NOT)
                self.state = 63
                self.condition(3)
                pass
            elif token in [20]:
                localctx = MiniQLParser.ParenCondContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(MiniQLParser.LPAREN)
                self.state = 65
                self.condition(0)
                self.state = 66
                self.match(MiniQLParser.RPAREN)
                pass
            elif token in [24]:
                localctx = MiniQLParser.CompCondContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.comparison()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 77
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MiniQLParser.OrCondContext(self, MiniQLParser.ConditionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 71
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 72
                        self.match(MiniQLParser.OR)
                        self.state = 73
                        self.condition(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniQLParser.AndCondContext(self, MiniQLParser.ConditionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 74
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 75
                        self.match(MiniQLParser.AND)
                        self.state = 76
                        self.condition(5)
                        pass

             
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ID(self):
            return self.getToken(MiniQLParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(MiniQLParser.ValueContext,0)


        def EQ(self):
            return self.getToken(MiniQLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniQLParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniQLParser.LT, 0)

        def GT(self):
            return self.getToken(MiniQLParser.GT, 0)

        def LTE(self):
            return self.getToken(MiniQLParser.LTE, 0)

        def GTE(self):
            return self.getToken(MiniQLParser.GTE, 0)

        def getRuleIndex(self):
            return MiniQLParser.RULE_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = MiniQLParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MiniQLParser.ID)
            self.state = 83
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 84
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniQLParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumberValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(MiniQLParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberVal" ):
                return visitor.visitNumberVal(self)
            else:
                return visitor.visitChildren(self)


    class IdValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniQLParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdVal" ):
                return visitor.visitIdVal(self)
            else:
                return visitor.visitChildren(self)


    class StringValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniQLParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MiniQLParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringVal" ):
                return visitor.visitStringVal(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = MiniQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = MiniQLParser.StringValContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(MiniQLParser.STRING)
                pass
            elif token in [23]:
                localctx = MiniQLParser.NumberValContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(MiniQLParser.NUMBER)
                pass
            elif token in [24]:
                localctx = MiniQLParser.IdValContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(MiniQLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




