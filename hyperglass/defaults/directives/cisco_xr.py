"""Default Cisco IOS-XR Directives."""

# Project
from hyperglass.models.directive import Rule, Text, BuiltinDirective

__all__ = (
    "CiscoXR_BGPASPath",
    "CiscoXR_BGPCommunity",
    "CiscoXR_BGPRoute",
    "CiscoXR_Ping",
    "CiscoXR_Traceroute",
)

CiscoXR_BGPRoute = BuiltinDirective(
    id="__hyperglass_cisco_xr_bgp_route__",
    name="BGP Route",
    rules=[
        Rule(
            condition="0.0.0.0/0",
            action="permit",
            command="show bgp ipv4 unicast {target}",
        ),
        Rule(
            condition="::/0",
            action="permit",
            command="show bgp ipv6 unicast {target}",
        ),
    ],
    field=Text(description="IP Address, Prefix, or Hostname"),
    platforms=["cisco_xr"],
)

CiscoXR_BGPASPath = BuiltinDirective(
    id="__hyperglass_cisco_xr_bgp_aspath__",
    name="BGP AS Path",
    rules=[
        Rule(
            condition="*",
            action="permit",
            commands=[
                "show bgp ipv4 unicast regexp {target}",
                "show bgp ipv6 unicast regexp {target}",
            ],
        )
    ],
    field=Text(description="AS Path Regular Expression"),
    platforms=["cisco_xr"],
)

CiscoXR_BGPCommunity = BuiltinDirective(
    id="__hyperglass_cisco_xr_bgp_community__",
    name="BGP Community",
    rules=[
        Rule(
            condition="*",
            action="permit",
            commands=[
                "show bgp ipv4 unicast community {target}",
                "show bgp ipv6 unicast community {target}",
            ],
        )
    ],
    field=Text(description="BGP Community String"),
    platforms=["cisco_xr"],
)

CiscoXR_Ping = BuiltinDirective(
    id="__hyperglass_cisco_xr_ping__",
    name="Ping",
    rules=[
        Rule(
            condition="0.0.0.0/0",
            action="permit",
            command="ping ipv4 {target} count 5 source {source4}",
        ),
        Rule(
            condition="::/0",
            action="permit",
            command="ping ipv6 {target} count 5 source {source6}",
        ),
    ],
    field=Text(description="IP Address, Prefix, or Hostname"),
    platforms=["cisco_xr"],
)

CiscoXR_Traceroute = BuiltinDirective(
    id="__hyperglass_cisco_xr_traceroute__",
    name="Traceroute",
    rules=[
        Rule(
            condition="0.0.0.0/0",
            action="permit",
            command="traceroute ipv4 {target} timeout 1 probe 2 source {source4}",
        ),
        Rule(
            condition="::/0",
            action="permit",
            command="traceroute ipv6 {target} timeout 1 probe 2 source {source6}",
        ),
    ],
    field=Text(description="IP Address, Prefix, or Hostname"),
    platforms=["cisco_xr"],
)