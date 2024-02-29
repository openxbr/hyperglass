"""Default Huawei Directives."""

# Project
from hyperglass.models.directive import Rule, Text, BuiltinDirective

__all__ = (
    "Huawei_BGPASPath",
    "Huawei_BGPCommunity",
    "Huawei_BGPRoute",
    "Huawei_Ping",
    "Huawei_Traceroute",
)

Huawei_BGPRoute = BuiltinDirective(
    id="__hyperglass_huawei_bgp_route__",
    name="BGP Route",
    rules=[
        Rule(
            condition="0.0.0.0/0",
            action="permit",
            command="display bgp routing-table {target}",
        ),
        Rule(
            condition="::/0",
            action="permit",
            command="display bgp ipv6 routing-table {target}",
        ),
    ],
    field=Text(description="IP Address, Prefix, or Hostname"),
    platforms=["huawei"],
)

Huawei_BGPASPath = BuiltinDirective(
    id="__hyperglass_huawei_bgp_aspath__",
    name="BGP AS Path",
    rules=[
        Rule(
            condition="*",
            action="permit",
            commands=[
                "display bgp routing-table regular-expression {target}",
                "display bgp ipv6 routing-table regular-expression {target}",
            ],
        )
    ],
    field=Text(description="AS Path Regular Expression"),
    platforms=["huawei"],
)

Huawei_BGPCommunity = BuiltinDirective(
    id="__hyperglass_huawei_bgp_community__",
    name="BGP Community",
    rules=[
        Rule(
            condition="*",
            action="permit",
            commands=[
                "display bgp routing-table community {target}",
                "display bgp ipv6 routing-table community {target}",
            ],
        )
    ],
    field=Text(description="BGP Community String"),
    platforms=["huawei"],
)

Huawei_Ping = BuiltinDirective(
    id="__hyperglass_huawei_ping__",
    name="Ping",
    rules=[
        Rule(
            condition="0.0.0.0/0",
            action="permit",
            command="ping -c 5 -a {source4} {target}",
        ),
        Rule(
            condition="::/0",
            action="permit",
            command="ping ipv6 -c 5 -a {source6} {target}",
        ),
    ],
    field=Text(description="IP Address, Prefix, or Hostname"),
    platforms=["huawei"],
)

Huawei_Traceroute = BuiltinDirective(
    id="__hyperglass_huawei_traceroute__",
    name="Traceroute",
    rules=[
        Rule(
            condition="0.0.0.0/0",
            action="permit",
            command="tracert -q 2 -f 1 -a {source4} {target}",
        ),
        Rule(
            condition="::/0",
            action="permit",
            command="tracert -q 2 -f 1 -a {source6} {target}",
        ),
    ],
    field=Text(description="IP Address, Prefix, or Hostname"),
    platforms=["huawei"],
)