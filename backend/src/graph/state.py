"""
Docstring for ComplianceQAPipeline.backend.src.graph.state
This file defines the state management for the graph pipeline

"""

import operator
from typing import TypedDict,Optional,Dict,Any,Annotated, List

# Define schema for a compliance issue state
class ComplianceIssue(TypedDict):
    """
    Defines the schema for output compliance 
    """
    category: str
    description: str # specific detail of violation
    severity: str # critical | warning
    timestamp: Optional[str]

class VideoAuditState(TypedDict):
    """
    Defines the schema of state that flows through langgraph
    """

    #Input features
    video_url: str 
    video_id: str #import for videoindexer

    #Ingestion and extraction data
    local_file_path: Optional[str] #stores the temporary file 
    video_metadata:Dict[str, Any] #{'duration':12,'file_name':'temp_file'}
    transcript: Optional[str] #text extracted from speech to text
    ocr_text: List[str] #text extracted from video using computer vision model

    #Analysis outpt
    #stores the list of compliances and using operator.add it appends to the list rather than replacing it
    compliance_report: Annotated[List[ComplianceIssue], operator.add] 

    #Final deliverables
    final_status: str 
    final_report: str

    #System observability (captures the list of system level crashes)
    error_report: Annotated[List[str], operator.add]





