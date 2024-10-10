# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: sigstore_bundle.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .....io import intoto as ____io_intoto__
from ...common import v1 as __common_v1__
from ...rekor import v1 as __rekor_v1__


@dataclass(eq=False, repr=False)
class TimestampVerificationData(betterproto.Message):
    """
    Various timestamped counter signatures over the artifacts signature.
    Currently only RFC3161 signatures are provided. More formats may be added
    in the future.
    """

    rfc3161_timestamps: List[
        "__common_v1__.Rfc3161SignedTimestamp"
    ] = betterproto.message_field(1)
    """
    A list of RFC3161 signed timestamps provided by the user. This can be used
    when the entry has not been stored on a transparency log, or in conjunction
    for a stronger trust model. Clients MUST verify the hashed message in the
    message imprint against the signature in the bundle.
    """


@dataclass(eq=False, repr=False)
class VerificationMaterial(betterproto.Message):
    """
    VerificationMaterial captures details on the materials used to verify
    signatures.
    """

    public_key: "__common_v1__.PublicKeyIdentifier" = betterproto.message_field(
        1, group="content"
    )
    x509_certificate_chain: "__common_v1__.X509CertificateChain" = (
        betterproto.message_field(2, group="content")
    )
    tlog_entries: List["__rekor_v1__.TransparencyLogEntry"] = betterproto.message_field(
        3
    )
    """
    An inclusion proof and an optional signed timestamp from the log. Client
    verification libraries MAY provide an option to support v0.1 bundles for
    backwards compatibility, which may contain an inclusion promise and not an
    inclusion proof. In this case, the client MUST validate the promise.
    Verifiers SHOULD NOT allow v0.1 bundles if they're used in an ecosystem
    which never produced them.
    """

    timestamp_verification_data: "TimestampVerificationData" = (
        betterproto.message_field(4)
    )
    """
    Timestamp may also come from
    tlog_entries.inclusion_promise.signed_entry_timestamp.
    """


@dataclass(eq=False, repr=False)
class Bundle(betterproto.Message):
    media_type: str = betterproto.string_field(1)
    """
    MUST be application/vnd.dev.sigstore.bundle+json;version=0.1 or
    application/vnd.dev.sigstore.bundle+json;version=0.2 when encoded as JSON.
    """

    verification_material: "VerificationMaterial" = betterproto.message_field(2)
    """
    When a signer is identified by a X.509 certificate, a verifier MUST verify
    that the signature was computed at the time the certificate was valid as
    described in the Sigstore client spec: "Verification using a Bundle". <http
    s://docs.google.com/document/d/1kbhK2qyPPk8SLavHzYSDM8-Ueul9_oxIMVFuWMWKz0E
    /edit#heading=h.x8bduppe89ln>
    """

    message_signature: "__common_v1__.MessageSignature" = betterproto.message_field(
        3, group="content"
    )
    dsse_envelope: "____io_intoto__.Envelope" = betterproto.message_field(
        4, group="content"
    )
    """
    A DSSE envelope can contain arbitrary payloads. Verifiers must verify that
    the payload type is a supported and expected type. This is part of the DSSE
    protocol which is defined here: <https://github.com/secure-systems-
    lab/dsse/blob/master/protocol.md>
    """