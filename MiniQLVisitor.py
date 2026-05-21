# Generated from C:/Users/ASUS/OneDrive/Desktop/lenguajes-programacion/miniQL/MiniQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniQLParser import MiniQLParser
else:
    from MiniQLParser import MiniQLParser

# This class defines a complete generic visitor for a parse tree produced by MiniQLParser.

class MiniQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniQLParser#program.
    def visitProgram(self, ctx:MiniQLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#LoadStatement.
    def visitLoadStatement(self, ctx:MiniQLParser.LoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#SelectStatement.
    def visitSelectStatement(self, ctx:MiniQLParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#SortStatement.
    def visitSortStatement(self, ctx:MiniQLParser.SortStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#ShowStatement.
    def visitShowStatement(self, ctx:MiniQLParser.ShowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#loadStmt.
    def visitLoadStmt(self, ctx:MiniQLParser.LoadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#selectStmt.
    def visitSelectStmt(self, ctx:MiniQLParser.SelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#sortStmt.
    def visitSortStmt(self, ctx:MiniQLParser.SortStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#showStmt.
    def visitShowStmt(self, ctx:MiniQLParser.ShowStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#AllColumns.
    def visitAllColumns(self, ctx:MiniQLParser.AllColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#NamedColumns.
    def visitNamedColumns(self, ctx:MiniQLParser.NamedColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#OrCond.
    def visitOrCond(self, ctx:MiniQLParser.OrCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#AndCond.
    def visitAndCond(self, ctx:MiniQLParser.AndCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#NotCond.
    def visitNotCond(self, ctx:MiniQLParser.NotCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#CompCond.
    def visitCompCond(self, ctx:MiniQLParser.CompCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#ParenCond.
    def visitParenCond(self, ctx:MiniQLParser.ParenCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#comparison.
    def visitComparison(self, ctx:MiniQLParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#StringVal.
    def visitStringVal(self, ctx:MiniQLParser.StringValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#NumberVal.
    def visitNumberVal(self, ctx:MiniQLParser.NumberValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniQLParser#IdVal.
    def visitIdVal(self, ctx:MiniQLParser.IdValContext):
        return self.visitChildren(ctx)



del MiniQLParser