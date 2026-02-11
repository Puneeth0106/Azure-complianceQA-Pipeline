"""
Docstring for ComplianceQAPipeline.backend.src.graph.state
This file defines the state management for the graph pipeline

"""

import operator
from typing import TypedDict,Optional,Dict,Any,Annotated, List

# Define schema for a compliance issue state
class ComplianceIssue(TypedDict):
    category: str
    description: str
    severity: str
    timestamp: str

class VideoState(TypedDict):

    #Input features
    video_url: str
    video_id: str

    #Ingestion and extraction data
    local_file_path: Optional[str]
    video_metadata:Dict[str, Any]
    transcript: Optional[str]
    ocr_text: List[str]

    #Analysis outpt
    compliance_report: Annotated[List[ComplianceIssue], operator.add]

    #Final deliverables
    final_status: str
    final_report: str

    #System observability
    error_report: Annotated[List[str], operator.add]





