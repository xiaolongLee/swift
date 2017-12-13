from Child import Child
from Node import Node  # noqa: I201

TYPE_NODES = [
    # simple-type-identifier -> identifier generic-argument-clause?
    Node('SimpleTypeIdentifier', kind='Type',
         children=[
             Child('Name', kind='Token',
                   token_choices=[
                       'IdentifierToken',
                       'CapitalSelfToken',
                       'AnyToken',
                   ]),
             Child('GenericArgumentClause', kind='GenericArgumentClause',
                   is_optional=True),
         ]),

    # member-type-identifier -> type '.' identifier generic-argument-clause?
    Node('MemberTypeIdentifier', kind='Type',
         children=[
             Child('BaseType', kind='Type'),
             Child('Period', kind='Token',
                   token_choices=[
                       'PeriodToken',
                       'PrefixPeriodToken',
                   ]),
             Child('Name', kind='Token',
                   token_choices=[
                       'IdentifierToken',
                       'CapitalSelfToken',
                       'AnyToken',
                   ]),
             Child('GenericArgumentClause', kind='GenericArgumentClause',
                   is_optional=True),
         ]),

    # array-type -> '[' type ']'
    Node('ArrayType', kind='Type',
         children=[
             Child('LeftSquareBracket', kind='LeftSquareBracketToken'),
             Child('ElementType', kind='Type'),
             Child('RightSquareBracket', kind='RightSquareBracketToken'),
         ]),

    # dictionary-type -> '[' type ':' type ']'
    Node('DictionaryType', kind='Type',
         children=[
             Child('LeftSquareBracket', kind='LeftSquareBracketToken'),
             Child('KeyType', kind='Type'),
             Child('Colon', kind='ColonToken'),
             Child('ValueType', kind='Type'),
             Child('RightSquareBracket', kind='RightSquareBracketToken'),
         ]),

    # metatype-type -> type '.' 'Type'
    #                | type '.' 'Protocol
    Node('MetatypeType', kind='Type',
         children=[
             Child('BaseType', kind='Type'),
             Child('Period', kind='PeriodToken'),
             Child('TypeOrProtocol', kind='IdentifierToken',
                   text_choices=[
                       'Type',
                       'Protocol',
                   ]),
         ]),

    # optional-type -> type '?'
    Node('OptionalType', kind='Type',
         children=[
             Child('WrappedType', kind='Type'),
             Child('QuestionMark', kind='PostfixQuestionMarkToken'),
         ]),

    # implicitly-unwrapped-optional-type -> type '!'
    Node('ImplicitlyUnwrappedOptionalType', kind='Type',
         children=[
             Child('WrappedType', kind='Type'),
             Child('ExclamationMark', kind='ExclamationMarkToken'),
         ]),

    Node('Initializer', kind='Syntax',
         children=[
             Child('Equal', kind='EqualToken'),
             Child('Value', kind='Expr'),
         ]),

    # tuple-type-element -> identifier? ':'? type-annotation ','?
    Node('TupleTypeElement', kind='Syntax',
         children=[
             Child('InOut', kind='InOutToken',
                   is_optional=True),
             Child('Name', kind='Token',
                   is_optional=True,
                   token_choices=[
                       'IdentifierToken',
                       'WildcardToken'
                   ]),
             Child('SecondName', kind='Token',
                   is_optional=True,
                   token_choices=[
                       'IdentifierToken',
                       'WildcardToken'
                   ]),
             Child('Colon', kind='ColonToken',
                   is_optional=True),
             Child('Type', kind='Type'),
             Child('Ellipsis', kind='Token',
                   is_optional=True),
             Child('Initializer', kind='Initializer',
                   is_optional=True),
             Child('TrailingComma', kind='CommaToken',
                   is_optional=True),
         ]),

    # tuple-type-element-list -> tuple-type-element tuple-type-element-list?
    Node('TupleTypeElementList', kind='SyntaxCollection',
         element='TupleTypeElement'),

    # tuple-type -> '(' tuple-type-element-list ')'
    Node('TupleType', kind='Type',
         children=[
             Child('LeftParen', kind='LeftParenToken'),
             Child('Elements', kind='TupleTypeElementList'),
             Child('RightParen', kind='RightParenToken'),
         ]),

    # throwing-specifier -> 'throws' | 'rethrows'
    # function-type -> attribute-list '(' function-type-argument-list ')'
    #   throwing-specifier? '->'? type?
    Node('FunctionType', kind='Type',
         children=[
             Child('LeftParen', kind='LeftParenToken'),
             Child('Arguments', kind='TupleTypeElementList'),
             Child('RightParen', kind='RightParenToken'),
             Child('ThrowsOrRethrowsKeyword', kind='Token',
                   is_optional=True,
                   token_choices=[
                       'ThrowsToken',
                       'RethrowsToken',
                   ]),
             Child('Arrow', kind='ArrowToken'),
             Child('ReturnType', kind='Type'),
         ]),

    # type-annotation -> attribute-list 'inout'? type
    Node('TypeAnnotation', kind='Syntax',
         children=[
             Child('Attributes', kind='AttributeList'),
             Child('InOutKeyword', kind='InoutToken',
                   is_optional=True),
             Child('Type', kind='Type'),
         ]),

    # protocol-composition-element-list -> protocol-composition-element
    #   protocol-composition-element-list?
    Node('ProtocolCompositionElementList', kind='SyntaxCollection',
         element='ProtocolCompositionElement'),

    # protocol-composition-element -> type-identifier '&'
    Node('ProtocolCompositionElement', kind='Syntax',
         children=[
             Child('ProtocolType', kind='Type'),
             Child('Ampersand', kind='AmpersandToken',
                   is_optional=True),
         ]),

    # generic-argument-list -> generic-argument generic-argument-list?
    Node('GenericArgumentList', kind='SyntaxCollection',
         element='GenericArgument'),

    # A generic argument.
    # Dictionary<Int, String>
    #            ^~~~ ^~~~~~
    Node('GenericArgument', kind='Syntax',
         children=[
             Child('ArgumentType', kind='Type'),
             Child('TrailingComma', kind='CommaToken',
                   is_optional=True),
         ]),

    # generic-argument-clause -> '<' generic-argument-list '>'
    Node('GenericArgumentClause', kind='Syntax',
         children=[
             Child('LeftAngleBracket', kind='LeftAngleToken'),
             Child('Arguments', kind='GenericArgumentList'),
             Child('RightAngleBracket', kind='RightAngleToken'),
         ]),

    # protocol-composition-type -> protocol-composition-elements
    Node('ProtocolCompositionType', kind='Type',
         children=[
             Child('Elements', kind='ProtocolCompositionElementList'),
         ]),
]
